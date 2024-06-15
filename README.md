### AutoDocMailer: A Simple Explanation

**AutoDocMailer** is a handy web app that helps you create and send personalized letters or circulars by using a template and filling in the necessary details automatically. Here’s how it works:

---

### How It Works

#### 1. **User Visits the Website 🖥️**

- **Home Page**: Users land on the home page of the app.
- **Form**: They see a simple form to fill in details like name, dates, place, etc.

#### 2. **User Fills Out the Form 📝**

- **Input Fields**: Users provide the required information, such as:
  - **Activity Name** (e.g., "Annual Meeting")
  - **From Date** (e.g., "2024-06-15")
  - **Year** (e.g., "2024")
  - **Date** (e.g., "2024-06-16")
  - **Place** (e.g., "Conference Room")
  - **Duration** (e.g., "2 hours")
  - **Day** (e.g., "Monday")
  - **Receiver's Email** (e.g., "example@domain.com")

#### 3. **Processing the Information 🛠️**

- **Submit**: User submits the form by clicking the submit button.
- **Data Handling**: The app collects the information and formats the dates.

#### 4. **Generating the Document 📄**

- **Template Loading**: The app loads a pre-defined Word document template.
- **Placeholder Replacement**: It replaces placeholders like `{{activityName}}` with the actual user-provided values.
- **Customization**: The app adjusts font sizes and other formatting aspects.

#### 5. **Emailing the Document 📧**

- **In-Memory Stream**: The customized document is saved in memory (no need to download it manually).
- **Email Setup**: The app sets up an email with the document as an attachment.
- **Send Email**: The app sends the email to the recipient's address.

#### 6. **User Gets Confirmation ✅**

- **Success Message**: The user sees a message indicating that the email has been sent successfully.

---

### Key Features

- **Automation**: Eliminates the need to manually edit and email the template every time.
- **Personalization**: Ensures each document is tailored to the specific details provided by the user.
- **Ease of Use**: Simple form submission and automatic processing make it user-friendly.

---

### Step-by-Step Process

1. **Go to AutoDocMailer**: Visit the app’s website.
2. **Fill Out the Form**: Enter the details you want in the letter.
3. **Submit**: Click the submit button to process your information.
4. **Receive Confirmation**: The app customizes the template and emails it to the recipient.
5. **Done!** 🎉: You’ve successfully sent a personalized letter!

---

### Technical Overview for Curious Minds 👨‍💻👩‍💻

- **Built with Flask**: A lightweight web framework for handling the server-side logic.
- **Uses Flask-Mail**: For sending emails via an SMTP server.
- **Template Management**: Uses a Word document template that’s loaded and customized on the fly.
- **Date Formatting**: Automatically formats dates to ensure consistency.
- **Security**: Uses environment variables to handle email credentials securely.

---

### Conclusion

**AutoDocMailer** simplifies the process of generating and sending personalized documents. Whether you need to send meeting invitations, circulars, or any other official communication, this app makes it quick and hassle-free. Just fill in the form, and let the app handle the rest!

Enjoy the ease and efficiency of **AutoDocMailer**! 🚀📬
