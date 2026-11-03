# SE8106 – Mobile Computing | Final Assignment
**Name:** Asjad Ahamed | **Reg No:** 20APSE4839

---

## Question 1 – User Authentication using Room Database (Android / Kotlin)

### Project Structure
```
Question1-AuthApp/
└── app/src/main/java/com/example/authapp/
    ├── MainActivity.kt
    ├── data/
    │   ├── User.kt
    │   ├── UserDao.kt
    │   └── AppDatabase.kt
    ├── navigation/
    │   └── Navigation.kt
    └── screens/
        ├── LoginScreen.kt
        ├── RegisterScreen.kt
        └── HomeScreen.kt
```

### How to run
1. Open **Android Studio** → *Open an existing project* → select `Question1-AuthApp/`
2. Make sure your `build.gradle.kts` includes the KSP plugin and Room / Navigation / Compose dependencies (see `app/build.gradle.kts`).
3. Click **Run ▶** (or `Shift+F10`) on an emulator or physical device running API 24+.

---

## Question 2 – Client–Server Communication using Sockets (Python)

### Project Structure
```
Question2-SocketChat/
├── Server.py
└── Client.py
```

### How to run

> Requires Python 3.6+ (no third-party libraries needed).

**Terminal 1 – start the server first:**
```bash
cd Question2-SocketChat
python3 Server.py
```

**Terminal 2 – connect the client:**
```bash
cd Question2-SocketChat
python3 Client.py
```

Type messages and press **Enter** to send. Type `exit` on either side to close the connection.

### Sample interaction
```
# Server console              # Client console
Server started on port 5000   Connected to server
Client connected
Server: Hello Client          Client: Hello Server
Client: Hello Server          Server: Hello Client
Server: I am fine.            Client: How are you?
Client: How are you?          Server: I am fine.
```

