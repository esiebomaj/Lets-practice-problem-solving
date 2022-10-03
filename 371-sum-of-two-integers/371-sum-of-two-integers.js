/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
    while (b !== 0){
        const [carry, sum] = [((a&b) << 1), a ^ b]
        a = sum
        b = carry
    }
    return a
};