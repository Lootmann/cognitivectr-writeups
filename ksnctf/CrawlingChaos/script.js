function hoge() {
  // weighted strings
  const ans = Array(
    70,
    152,
    195,
    284,
    475,
    612,
    791,
    896,
    810,
    850,
    737,
    1332,
    1469,
    1120,
    1470,
    832,
    1785,
    2196,
    1520,
    1480,
    1449
  );

  const flag = [];

  for (var i = 0; i < ans.length; i++) {
    const ch = ans[i] / (i + 1);
    flag.push(String.fromCharCode(ch));
  }

  console.log(flag.join(""));
}

hoge();
