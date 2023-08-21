function isPrime(number) {
    if (number <= 1) {
        return false;
    }
    
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            return false;
        }
    }
    
    return true;
}

function findPrimesInRange(start, end) {
    const primes = [];
    for (let num = start; num <= end; num++) {
        if (isPrime(num)) {
            primes.push(num);
        }
    }
    return primes;
}

const startRange = 1;
const endRange = 50;
const primeNumbers = findPrimesInRange(startRange, endRange);

console.log(`Prime numbers between ${startRange} and ${endRange}:`);
console.log(primeNumbers);
