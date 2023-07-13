# Macagotchi  (For macOS)

Macagotchi is a virtual pet application that runs on a computer (Windows codebase is here). It interacts with the user by displaying a virtual pet on the screen while it scans for nearby Wi-Fi networks, and it will become happy when it’s found new SSIDs. Your Macagotchi will also track how many days in a row you’ve been able to keep it happy, unlocking changes to the UI. While the code is very different, the idea is based on the excellent pwnagotchi project. The difference here is that Macagothchi doesn’t do anything sinister which might get you arrested or annoy people sitting around you. But seriously, check it out.

As pwnagotchi’s less sinister cousin it only collects SSIDs to keep score, which it keeps locally in a hashed log. It doesn’t export data, and doesn’t contain any marketing or tracking code. By design, if you want to share how many SSIDs you’ve collected and/or how happy your Macagotchi is, take a screenshot.

If you’d prefer not to do a step by step install of the source code, you can download the finished installers: for macOS and PC.

A Raspberry Pi version is currently in development and I’ll be releasing the code and hardware specs very soon.


## Functionalities:
1. ### Display a virtual pet on the screen:
   - The program displays a virtual pet image that represents the current state of the pet.
   - The pet's image changes based on various conditions and events.

2. ### Naming:
   - Users can press fn+F2 to edit their Macagotchi’s name and press return to save it.

3. ### Wi-Fi Network Scanning:
   - The program scans for nearby Wi-Fi networks using the built-in airport utility on macOS.
   - It retrieves the list of network SSIDs 
   - Scanned networks are hashed and then stored in a file for future reference.

4. ### Loyalty and Streak Tracking:
   - Macagotchi will remember how many days in a row the user has been keeping it happy, unlocking UI updates.

5. ### Displaying Feedback:
   - Macagotchi will become happy, friendly or hungry depending on how well you feed it.
   - Your Macagotchi will leave messages on the screen, explaining to users how it feels and giving you suggestions on how to help it feel better. For example, when a Macagotchi is hungry, the on screen message might say “Can we go on a walk?”, or when your Macagotchi is waking up, the message might read “I’ve been asleep for x days.”


## Dependencies:
- ### [Python 3.x](https://www.python.org/)
- ### [pygame library](https://www.pygame.org/news)

## External Files:
- **logo.png:** Represents the logo image used for the program.
- **logo.ico:** Used for packaging in PyInstaller to produce the icon of the .app or .exe
- **address.txt:** Stores the hashed addresses of scanned Wi-Fi networks.
- l**ongestStreak.txt**: Stores the longest streak of consecutive program usage.
- **stats.txt**: Stores the Macagotchi’s name.
- **loyalty.txt**: Stores dates of consecutive program usage.
- **totalLog.txt**: Stores the total number of Wi-Fi networks scanned.


## Build:
If you want to skip the manual build, you can download the finished installers for free at itch.io: here for [macOS and Windows](https://spacemonkeyalfa.itch.io/macagotchi).  Raspeberry Pi coming soon!


## License:
[MIT LICENSE](https://github.com/SpaceMonkeyAlfa/macagotchi-macos/blob/main/LICENSE)
