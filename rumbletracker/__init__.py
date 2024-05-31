from .cog import EmbedTracker


async def setup(bot):
    await bot.add_cog(EmbedTracker(bot))