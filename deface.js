document.documentElement.innerHTML = `
<!DOCTYPE html>
<html>
<head>
<title>defaced</title>
<style>
body {
    margin: 0;
    height: 100vh;
    background: black;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
}
h1 {
    color: #00ff00;
    font-size: 40px;
    text-align: center;
}
</style>
</head>
<body>
<h1>defaced by pentester team</h1>
</body>
</html>
`;
