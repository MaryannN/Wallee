const wiki = require('wikipedia');
document.getElementById("submit").addEventListener("click", async () => {
try { 
    let input = document.getElementById("insert").value;
    const summary = await wiki.summary(input);
    alert(input);
    let extract = summary.extract;
    extract = extract.split(". ").filter((val, index) => index < 3).join(". ");
    alert(extract); //wiki definition
    return extract;
}catch(error){
    alert(error); //type of wiki error
}});
