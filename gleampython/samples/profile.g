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

node script(src='gleam_profile.js')

profile(name='Colin', age=26)
profile(name='Holly', age=22)

node p(id="clickhere" onclick="alert(\"hello\"") "Click here to generate more profiles using JS"
