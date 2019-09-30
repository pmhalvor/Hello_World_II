This was a data scrapping project found on [Towards Data Science](https://towardsdatascience.com/master-python-through-building-real-world-applications-part-6-d05a7ea58a23).

The first file <code> player_ids.py</code> pulls the ids of all the players in the 2018 FIFA World Cup. These will later be using to access each player's corresponding team information from a distinct url in the next file.

The next file ```player_info.py``` pulls general information on the player, like country, position, etc.

The final file ```play_stats.py``` uses the ids gathered in the first file to access the distinct stats url corresponding to each play.
