/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  var value = init;
  return {
    increment: function() {
      value += 1;
      return value;
    },
    decrement: function() {
      value -= 1;
      return value;
    },
    reset: function() {
      value = init;
      return value;
    }
  };
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */