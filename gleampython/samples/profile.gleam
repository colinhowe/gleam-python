macro profile(name, age) {
    node div {
        node p {
            node span "Name: "
            node span name
        }
        node p {
            node span "Age: "
            node span age
        }
    }
}

profile(name='Colin', age=26)
profile(name='Holly', age=24)

node h3 "New profiles appear below"
node div(id="container", style="padding: 10px; border: 2px dashed #ddd") ""

node span(onclick="$gleam.insertView('samples/profile', 'container')") "Click here"
