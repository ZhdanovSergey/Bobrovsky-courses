namespace OOAP_2._8;

delegate Message MessageBuilder(string text);
delegate void EmailReceiver(EmailMessage message);

class Message
{
    public string Text { get; }
    public Message(string text) => Text = text;
    public virtual void Print() => Console.WriteLine($"Message: {Text}");
}
class EmailMessage : Message
{
    public EmailMessage(string text) : base(text) { }
    public override void Print() => Console.WriteLine($"Email: {Text}");
}
class SmsMessage : Message
{
    public SmsMessage(string text) : base(text) { }
    public override void Print() => Console.WriteLine($"Sms: {Text}");
}

class Client
{
    void Main()
    {
        EmailMessage WriteEmailMessage(string text) => new EmailMessage(text);
        void ReceiveMessage(Message message) => message.Print();

        // делегату с базовым типом передаем метод с производным типом
        MessageBuilder messageBuilder = WriteEmailMessage; // ковариантность
        Message message = messageBuilder("Hello");
        message.Print();    // Email: Hello

        // делегату с производным типом передаем метод с базовым типом
        EmailReceiver emailBox = ReceiveMessage; // контравариантность
        emailBox(new EmailMessage("Welcome"));  // Email: Welcome
    }
}