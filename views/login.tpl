%rebase('base.tpl')
<div class="container">
    <div class="row">
        <p id="login"><b>Log-in</b></p>
        <div id="login-error" class="{{errors}} card-panel #ff5252 red accent-2">
            <i class="Tiny material-icons">lock</i>
            <span>Login Failed, please try again</span>
        </div>
        <form action="/login" method="post" id="loginform" name="loginform">
            <input id="nick" name="nick" type="text" placeholder="Nickname">
            <input id="password" name="password" type="password" placeholder="Password">
            <input class="btn waves-effect waves-light" type="submit" value="Login">
        </form>
    </div>
</div>