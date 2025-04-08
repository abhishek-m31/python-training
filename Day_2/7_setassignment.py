most_polluted = {'Delhi','Mumbai','Pune','Banglore','Calcutta','Srinagar'}
densly_populated= {'Mumbai','Banglore','Calcutta','Chennai','Varanasi','Kanpur'}

densly_populated_polluted = densly_populated & most_polluted
print(densly_populated_polluted)

densly_populated_notpolluted = densly_populated - most_polluted
print(densly_populated_notpolluted)

densly_populated_or_polluted= densly_populated | most_polluted
print(densly_populated_or_polluted)

condition4 = (most_polluted - densly_populated) | (densly_populated - most_polluted)
print(condition4)