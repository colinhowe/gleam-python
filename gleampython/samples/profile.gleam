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
