def solution(players, callings):
    playersDict = { player: rank for rank, player in enumerate(players) }
    
    for call in callings:
        idx, pre = playersDict[call], playersDict[call]-1
        
        playersDict[players[idx]] -= 1
        playersDict[players[pre]] += 1
        players[idx], players[pre] = players[pre], players[idx]
    
    return players