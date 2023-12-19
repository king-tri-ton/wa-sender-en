## WhatsApp Sender

WhatsApp Sender is a program built on the original codebase of [alright](https://github.com/Kalebu/alright) by [Kalebu](https://github.com/Kalebu). It allows users to send bulk messages on WhatsApp.

---

### Version 2

#### Features and Changes:

1. **User Interface Transition:**
   - Migrated from Tkinter to PyQt5 for the graphical user interface.
   - Improved layout and design for a more modern look.

2. **File Handling:**
   - Utilized QTextEdit for file paths to enhance readability and ease of use.
   - Implemented QFileDialog for a more user-friendly file selection process.

3. **Log Display:**
   - Replaced ScrolledText with QTextEdit for the log display.
   - Introduced QTextEdit for better log readability.

4. **Threading:**
   - Implemented QThread for improved concurrency and responsiveness.
   - Enhanced thread management for a smoother user experience.

5. **User Instructions:**
   - Incorporated QLabel for instruction messages to enhance clarity.
   - Improved wording for better user understanding.

6. **Code Structure:**
   - Refactored code to align with PyQt5 standards.
   - Enhanced comments for improved code readability.

7. **Miscellaneous:**
   - Added icon functionality for the application window.
   - Improved copyright display and added a GitHub link.

---

### How to Use:

1. **Select Contacts:**
   - Click the "Обзор" button to choose a text file containing WhatsApp contacts.

2. **Compose Message:**
   - Enter the message you want to send in the "Введите сообщение" text area.

3. **Start Newsletter:**
   - Click the "Начать рассылку" button to begin sending messages.
   - Do not close the program until the newsletter is complete.

4. **Logs:**
   - The "Логи" section displays the progress and results of the newsletter.

5. **Closing the Program:**
   - If the newsletter is in progress, the program will prompt you to confirm closure.

6. **Copyright and GitHub:**
   - The program is © 2023 King Triton.
   - Visit the [GitHub repository](https://github.com/king-tri-ton/wa-sender-en) for more information.

---

### Acknowledgments:

This program is based on the alright project by Kalebu. Special thanks to Kalebu for providing the original codebase.

Feel free to contribute to the project by providing feedback, reporting issues, or submitting pull requests on the GitHub repository.

---

*© 2023 King Triton*