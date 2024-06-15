### Exciting Update! 🌟

Hey there, everyone! It’s me, **Gc**.

I’m excited to share that I’ve created **AutoDocMailer**, a super-efficient web app using the Flask framework. It automates the creation and emailing of personalized letters by simply using a template and the details you provide. 

You no longer need to manually edit and send out templates each time you have a new letter to send. Just fill out a form with the necessary details and edit the template.docx with your required docx, and **AutoDocMailer** will handle the rest!

Here’s the best part: If you ever run into any bugs or issues, don’t hesitate to reach out. I’m here to help you resolve them. Go ahead and enjoy the convenience of automated document handling!

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

### Setting Up Your App Password from Google 🔒

For **AutoDocMailer** to send emails on your behalf using your Google account, you need to generate an app password. Here’s how:

1. **Go to Google Account**:
   - Visit [Google Account](https://myaccount.google.com/).

2. **Sign In**:
   - Sign in with your Google credentials if you're not already logged in.

3. **Navigate to Security Settings**:
   - In the left sidebar, click on **Security**.

4. **Turn On 2-Step Verification** (if not already enabled):
   - Under the **"Signing in to Google"** section, click **2-Step Verification** and follow the prompts to enable it.

5. **Generate App Password**:
   - Return to the **Security** page.
   - Scroll down to **"App passwords"** and click it.
   - Sign in again if prompted.
   - In the **Select app** dropdown, choose **Mail**.
   - In the **Select device** dropdown, choose **Other (Custom name)**.
   - Enter a name (e.g., "AutoDocMailer") and click **Generate**.

6. **Copy the App Password**:
   - A 16-character password will be shown. Copy it.

7. **Use the App Password**:
   - In your `.env` file for **AutoDocMailer**, set the `SENDER_MAIL_APP_PASSWORD` to this app password.
  
Refer this video for furthur doubts - https://youtu.be/nOkpTwPvDTg?si=lNL0noZNaSgI7CHG


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


Enjoy the ease and efficiency of **AutoDocMailer**! 🚀📬

Happy coding and have a blast! 🎉

Cheers, **Gc**
