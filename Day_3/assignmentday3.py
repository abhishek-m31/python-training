colours = {'Blue': 85, 'Red': 70, 'White': 60, 'Purple': 75, 'Green': 40}
print(colours)

popular_filter = dict(filter(lambda item: item[1]))
print(popular_filter)

min_popular = min(colours.items(), key=lambda item: item[1])
print(min_popular)

max_popular = max(colours.items(), key=lambda item: item[1])
print(max_popular)

