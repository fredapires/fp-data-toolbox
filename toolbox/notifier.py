# %% --- jupyter_helpers notifications setup
def setup():
    from IPython.display import Audio
    from jupyter_helpers.desktop_integration import DesktopIntegration
    class WindowsIntegration(DesktopIntegration):
        def notify(self, title, text, notify_id=None, show_again=True, urgency='normal'):
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(title, text)
        def notify_close(self, notify_id):
            pass
    from jupyter_helpers.notifications import Notifications
    Notifications(
        time_threshold = 60, # threshold for notification in seconds
        integration = WindowsIntegration
    );
