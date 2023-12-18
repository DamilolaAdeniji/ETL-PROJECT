def extraction_error(message_list):
    error_message = ' '.join(message_list)
    return f"""
        <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>

        <body style="font-family: Arial, sans-serif;">

        <p>Hello Dammy,</p>

        <p> Your pipeline failed because the data could not be extracted from the github repo. Please review your code and retry <p>
        <p> {error_message} <p>
        <p>Warm regards,<br>
        <p>Best Analytics
        </body>
        """

def transformation_error(message_list):
    error_message = ' '.join(message_list)
    return f"""
        <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>

        <body style="font-family: Arial, sans-serif;">

        <p>Hello Dammy,</p>

        <p> Your pipeline failed because an error occured during transformation. Please review your code and retry <p>
        <p> {error_message} <p>
        <p>Warm regards,<br>
        <p>Best Analytics
        </body>
        """

def loading_error(message_list):
    error_message = ' '.join(message_list)
    return f"""
        <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>

        <body style="font-family: Arial, sans-serif;">

        <p>Hello Dammy,</p>

        <p> Your pipeline failed because an error occured during the loading process. Please review your code and retry <p>
        <p> {error_message} <p>
        <p>Warm regards,<br>
        <p>Best Analytics
        </body>
        """