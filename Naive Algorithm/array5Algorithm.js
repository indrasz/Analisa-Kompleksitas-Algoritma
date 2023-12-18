function areArraysEqualNaive(n, m) {
    if (n.length !== m.length) {
        return false;
    }

    for (let i = 0; i < n.length; i++) {
        if (n[i] !== m[i]) {
            return false;
        }
    }

    return true;
}

const startTimeNaive = performance.now();
const kata1 = ['a', 'b', 'c', 'd', 'e'];
const kata2 = ['a', 'b', 'c', 'd', 'e'];
console.log(areArraysEqualNaive(kata1, kata2));
const endTimeNaive = performance.now();
console.log(`Algoritma pertama = Waktu eksekusi Algoritma Naive: ${endTimeNaive - startTimeNaive} milidetik`);
