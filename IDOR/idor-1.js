const express = require('express');
const app = express();
app.use(express.json());
//Ali-HZ
// Simulated in-memory database.
const users = [
    { id: 100, Fname: "Victim", Lname: "User" }, // Victim
    { id: 1, Fname: "Attacker", Lname: "User" }  // Attacker (logged-in user)
];

// Middleware to simulate authentication via JWT
app.use((req, res, next) => {
    req.user = { id: 1 }; // The logged-in attacker has ID 1
    next();
});

app.post('/editProfile', (req, res) => {
    const inputId = req.body.id;
    const userExists = users.some(user => user.id == inputId);

    if (userExists) {
        if (req.user.id != inputId) {
            return res.status(403).send("Forbidden: You cannot edit this profile.");
        }
    }

    const user = users.find(user => user.id == parseInt(inputId));
    if (!user) {
        return res.status(404).send("User not found.");
    }

    user.Fname = req.body.Fname || user.Fname;
    user.Lname = req.body.Lname || user.Lname;

    return res.send(`Profile updated for user id ${user.id}.\n ${user.Fname} , ${user.Lname}`);
});

app.listen(3000, () => console.log("Server running on port 3000"));