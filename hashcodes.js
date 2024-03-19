/* hashcodes.js */
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const string = document.querySelector('#string').value;
    const hashcode = hashCode(string);
    document.querySelector('#hashcode').innerText = hashcode;
});