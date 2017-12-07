int possibleSums(int[] coins, int[] quantity) {
	HashSet<Integer> possibleSums = new HashSet<Integer>();
	possibleSums.add(0);

	for(int i = 0; i < coins.length; i++){
		for (int j = 0; j < quantity[i]; j++){
			HashSet<Integer> possibleSumsBeforeIteration = new HashSet<Integer>(possibleSums);
			for (int possibleSum : possibleSumsBeforeIteration){
				possibleSums.add(possibleSum + coins[i]);
			}
		}
	}
	return possibleSums.size();
}