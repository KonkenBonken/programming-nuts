const isPrime = n => {
	let prime = true;
	for (var i = 2; i < Math.max(Math.sqrt(n)); i++)
		if (n % i == 0) {
			prime = false;
			break;
		}
	return prime;
}