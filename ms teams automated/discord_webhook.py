from discord_webhooks import DiscordWebhooks

#Put your discord webhook url here.
webhook_url = 'https://discord.com/api/webhooks/824008222536499250/7rjIZ44aJ6J_D2YIBmAP9DgB26Fl4refjAQxlzeP4qcxxw-8l2KhHlyxT4zeU0LFu0Hm'


def send_msg(class_name,status,start_time,end_time):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- Sahil Saleem')

    if(status=="joined"):

      webhook.set_content(title='Class Joined Succesfully',
                          description="Here's your report")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Joined at', value=start_time)
      webhook.add_field(name='Leaving at', value=end_time)

    elif(status=="left"):
      webhook.set_content(title='Class left Succesfully',
                          description="Here's your report")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Joined at', value=start_time)
      webhook.add_field(name='Left at', value=end_time)


    elif(status=="noclass"):
      webhook.set_content(title='Seems like no class today',
                          description="No join button found! Assuming no class.")

      # Appends a field
      webhook.add_field(name='Class', value=class_name)
      webhook.add_field(name='Status', value=status)
      webhook.add_field(name='Expected Join time', value=status)
      webhook.add_field(name='Expected Leave time', value=end_time)

    webhook.send()

    print("Sent message to discord")
