function compareWordsAlgorithm1(input1, input2) {
    const startTime = performance.now();

    for (let i = 0; i < input1.length; i++) {
        for (let j = 0; j < input2.length; j++) {
            if (input1[i] === input2[j]) {
                const endTime = performance.now();
                console.log("Result Algorithm 1:", true);
                console.log("Time taken by Algorithm 1:", endTime - startTime, "milliseconds");
                return true;
            }
        }
    }

    const endTime = performance.now();
    console.log("Result Algorithm 1:", false);
    console.log("Time taken by Algorithm 1:", endTime - startTime, "milliseconds");
    return false;
}

function compareWordsAlgorithm2(input1, input2) {
    const startTime = performance.now();

    const set1 = new Set(input1);
    const set2 = new Set(input2);

    const commonWords = new Set([...set1].filter(word => set2.has(word)));

    const endTime = performance.now();
    const result = commonWords.size > 0;
    console.log("Result Algorithm 2:", result);
    console.log("Time taken by Algorithm 2:", endTime - startTime, "milliseconds");
    return result;
}

// Contoh penggunaan
const input1 = ["saya", "suka", "dengan", "anda", "sebagainya"];
const input2 = ["aku", "dan", "kamu", "tidak", "cocok", "anda"];

const input3 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"];
const input4 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "anda"];

const input5 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"];
const input6 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "anda", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"];

const input7 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"];
const input8 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "anda", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"];

const input9 = ["saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya", "saya", "suka", "dengan", "anda", "sebagainya"];
const input10 = ["aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "anda", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok", "aku", "dan", "kamu", "tidak", "cocok"];

compareWordsAlgorithm1(input1, input2);
compareWordsAlgorithm2(input1, input2);
console.log("====================================");
compareWordsAlgorithm1(input3, input4);
compareWordsAlgorithm2(input3, input4);
console.log("====================================");
compareWordsAlgorithm1(input5, input6);
compareWordsAlgorithm2(input5, input6);
console.log("====================================");
compareWordsAlgorithm1(input7, input8);
compareWordsAlgorithm2(input7, input8);
console.log("====================================");
compareWordsAlgorithm1(input9, input10);
compareWordsAlgorithm2(input9, input10);