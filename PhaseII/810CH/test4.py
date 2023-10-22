''' Test 4 - https://chat.openai.com/share/df07e19e-fd72-4fcd-b3a6-60de92daab3f - convo link '''
# Rated 0.74
from typing import Optional
from discord.errors import Forbidden
from discord.commands import Option, SlashCommandGroup
from discord.ext import commands
import discord
import util
from blitzdb import Document, FileBackend
from datetime import datetime

class ReminderEntry(Document):
    pass

class InteractedUser(Document):
    pass

class Reminder(commands.Cog):
    reminder = SlashCommandGroup(
        "reminder", "Set reminders for yourself or publicly", guild_ids=util.guilds
    )

    def __init__(self, bot):
        self.bot = bot
        self.backend = FileBackend("db")
        self.backend.autocommit = True

    async def send_first_time_disclaimer(self, ctx: discord.ApplicationContext):
        user = ctx.author
        interacted = self.backend.filter(InteractedUser, {'user_id': user.id})
        if not interacted:
            try:
                await user.send("This is a best-effort service. Don't use it for anything critical.")
            except Forbidden:
                await ctx.send("Private messages from server members seem to be disabled. Please enable this setting to receive the disclaimer.")
                return
            new_user = InteractedUser({'user_id': user.id})
            self.backend.save(new_user)

    @reminder.command(
        name="add",
        description="Adds a new reminder",
        guild_ids=util.guilds
    )
    async def add(
            self,
            ctx: discord.ApplicationContext,
            message: Option(str, description="The reminder message"),
            time_unit: Option(str, description="Time unit, e.g., 'minutes', 'hours', 'days'")
    ):
        await self.send_first_time_disclaimer(ctx)
        reminder_entry = ReminderEntry({
            "message": message,
            "time_unit": time_unit,
            "creator_id": ctx.author.id,
            "creation_time": datetime.now()
        })
        self.backend.save(reminder_entry)
        await ctx.send(f"Reminder set for {message} in {time_unit}")

    @reminder.command(
        name="clear",
        description="Clears all reminders",
        guild_ids=util.guilds
    )
    async def clear(
            self,
            ctx: discord.ApplicationContext
    ):
        user_id = ctx.author.id
        reminders_to_clear = self.backend.filter(ReminderEntry, {"creator_id": user_id})
        for reminder in reminders_to_clear:
            self.backend.delete(reminder)
        await ctx.send("All your reminders have been cleared.")

def setup(bot):
    bot.add_cog(Reminder(bot))

@tasks.loop(seconds=60)
async def check_reminders(self):
    now = datetime.utcnow()
    all_reminders = self.backend.filter(ReminderEntry, {})
    for reminder in all_reminders:
        reminder_time = reminder['time']
        if reminder_time <= now:
            channel = self.bot.get_channel(reminder["channel_id"])
            user = self.bot.get_user(reminder["user_id"])
            if reminder["location"] == "private":
                await user.send(reminder["text"])
            else:
                await channel.send(
                    f"{user.mention}, A reminder for you: {reminder['text']}"
                )
            self.backend.delete(reminder)