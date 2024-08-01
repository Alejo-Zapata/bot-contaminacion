import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def remplazoplastico(ctx):
    await ctx.send("""
Existen varios materiales que se pueden utilizar como sustitutos del plástico, 
como el papel, las fibras naturales (como el algodón, el cáñamo o el yute) y las bolsas reutilizables hechas de materiales reciclados (como el nylon o el poliéster)
por ejemplo usar bolsas de tela o envases o frascos de vidrio
""")

@bot.command()
async def desperdicioalimentario(ctx):
    await ctx.send("""
Reducir el desperdicio alimentario es importante, por varias razones. 
Mejora la nutrición y la seguridad alimentaria mundial, ya que proporciona una dieta saludable a una población en crecimiento.
Además, reduce las emisiones de gases de efecto invernadero y ahorra financieramente para empresas y consumidores.
""")
    
@bot.command()
async def residuoselectronicos(ctx):
    await ctx.send("""
El reciclaje de estos aparatos tiene muchos beneficios ambientales. 
Permite recuperar elementos (como vidrio, plástico y metales) que vuelven al ciclo productivo. 
Esto disminuye la extracción de materias primas, cuidando los recursos naturales
y reduce la contaminación del aire, el agua y el suelo.
""")
    
@bot.command()
async def reutilizarenvases(ctx):
    await ctx.send("""
Reutilizar envases o recipientes es importante porque reduce el uso de materias primas, 
alarga la vida útil de los envases, ahorra para el consumidor y reduce la huella de carbono.
""")
    
bot.run("")
