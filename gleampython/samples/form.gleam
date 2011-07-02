macro user_profile(user) {
    node span 'User name: ' + user.name
    node a(href='#') 'view profile'
}

for user in c.users {
    user_profile(user)
}
