function areArraysEqualOptimized(n, m) {
    if (n.length !== m.length) {
        return false;
    }

    const sortedN = n.slice().sort();
    const sortedM = m.slice().sort();

    for (let i = 0; i < n.length; i++) {
        if (sortedN[i] !== sortedM[i]) {
            return false;
        }
    }

    return true;
}

const startTimeOptimized = performance.now();
const kata3 = ['a'];
const kata4 = ['a'];
console.log(areArraysEqualOptimized(kata3, kata4));
const endTimeOptimized = performance.now();
console.log(`Algortima kedua = Waktu eksekusi Algoritma Optimized: ${endTimeOptimized - startTimeOptimized} milidetik`);

