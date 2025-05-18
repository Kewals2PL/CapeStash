# THE PLAN:

## CLOSE-ish FUTURE:

1.  Get a list of capes that were unlockable by a code `[key]` - undoable as there is no up-to-date list of every claimable cape, although I could update the list every time a new cape comes around.
2.  Make an HTML file that looks like this:
    ```
    ---------------------------------------------------------
    |                                                       |
    |   -----------     Cape Name                           |
    |   | cape    |         -----------------------------   |
    |   | preview | Get Key:|   Pass Req        |Ok     |   |
    |   | here    |         |                   |Button |   |
    |   -----------         -----------------------------   |
    ---------------------------------------------------------
    ```
3.  Make a script that generates a one-time use pass (for the "Pass Req" section indicated above).

## FAR FUTURE:

4.  SOMEHOW host the HTML file onto the web (desired domain/subdomain: `index.capes.mc`) and make it search for new passwords, capes, etc.
5.  How hosting on the web would work:
    ```
    ---------------------------------------------------------------------------------------------------------------------
    My PC ----> GitHub
    |           |
    |           |
    |           |
    |           v (Pushes/Updates)
    |-------> Hosting Server ----> Web
    |                                ^
    |                                | (Content served to users)
    ----------------------------------(Cycle implies My PC manages/updates what's on GitHub, which deploys to Hosting)
    ```
