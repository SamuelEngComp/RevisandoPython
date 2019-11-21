import pygal

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'BANCAS INTERNACIONAIS'


worldmap_chart.add('PORTUGAL', ['pt'])
worldmap_chart.add('BRASIL', ['br'])
worldmap_chart.add('MEXICO', ['mx'])
worldmap_chart.add('ESTADOS UNIDOS', ['us'])
worldmap_chart.add('AUSTRALIA', ['au'])
worldmap_chart.add('MOCAMBIQUE', ['mz'])
worldmap_chart.add('INGLATERRA', ['gb'])
worldmap_chart.add('CANADA', ['ca'])

worldmap_chart.render_in_browser()