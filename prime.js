function _doesNotExist(val) {
  if (val == null || val == undefined) {
      return true
  } else {
      return false
  }
}

console.log(`${_doesNotExist()}`);