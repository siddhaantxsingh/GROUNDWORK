# webbrowser

## webbrowser.BackgroundBrowser(name)

Class for all browsers which are to be started in the background.

## webbrowser.BaseBrowser(name='')

Parent class for all browsers. Do not use directly.

## webbrowser.Chrome(name='')

Launcher class for Google Chrome browser.

## webbrowser.Chromium(name='')

Launcher class for Google Chrome browser.

## webbrowser.Edge(name='')

Launcher class for Microsoft Edge browser.

## webbrowser.Elinks(name='')

Launcher class for Elinks browsers.

## webbrowser.Epiphany(name='')

Launcher class for Epiphany browser.

## webbrowser.GenericBrowser(name)

Class for all browsers started with a command and without remote functionality.

## webbrowser.Konqueror(name='')

Controller for the KDE File Manager (kfm, or Konqueror). See the output of ``kfmclient --commands``
for more information on the Konqueror remote-control interface.

## webbrowser.Mozilla(name='')

Launcher class for Mozilla browsers.

## webbrowser.Opera(name='')

Launcher class for Opera browser.

## webbrowser.UnixBrowser(name='')

Parent class for all Unix browsers with remote functionality.

## webbrowser.get(using=None)

Return a browser launcher instance appropriate for the environment.

## webbrowser.open(url, new=0, autoraise=True)

If possible, open url in a location determined by new.
- 0: the same browser window (the default).
- 1: a new browser window.
- 2: a new browser page ("tab").
If possible, autoraise raises the window (the default) or not.

If opening the browser succeeds, return True.
If there is a problem, return False.

## webbrowser.open_new(url)

Open url in a new window of the default browser. If not possible, then open url in the only browser window.

## webbrowser.open_new_tab(url)

Open url in a new page ("tab") of the default browser. If not possible, then the behavior becomes equivalent to open_new().

## webbrowser.register(name, klass, instance=None, *, preferred=False)

Register a browser connector.
