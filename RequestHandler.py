from flask import Flask, render_template, request

class RequestHandler:

    def HandleError(value):
        return render_template('Failure.html',value=value)

    def successfull_entry(value):
        return render_template('result.html', value=value)


