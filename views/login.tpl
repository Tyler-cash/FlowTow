%rebase('base.tpl')
<div class="container">
    <div class="row">
        <p id="login"><b>Log-in</b></p>
        <form action="/login" method="post">
            <input id="nick" name="nick" type="text" placeholder="Nickname">
            <input id="password" name="password" type="password" placeholder="Password">
            <input class="btn waves-effect waves-light" type="submit" value="Login">
        </form>
    </div>
</div>