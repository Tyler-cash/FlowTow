<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{{title}}</title>

    <!--Jquery compiled and minified-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0-beta1/jquery.min.js"></script>
    <!-- Compiled and minified CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/css/materialize.min.css">
    <!--Stylesheet css-->
    <link rel="stylesheet" href="/static/css/stylesheet.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <!-- Compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.5/js/materialize.min.js"></script>
    <script src="/static/js/script-index.js"></script>
</head>
<body>

<div class="navbar-fixed ">
    <nav>
        <div class="nav-wrapper #546e7a blue-grey darken-1">
            <a href="#" class="brand-logo center">FlowTow</a>
            <ul>
                <li id="nav-home"><a href="/">Home</a></li>
                <li id="nav-about"><a href="/about">About</a></li>
                <li class="{{loggedIn}}" id="nav-profile"><a href="/my">My Images</a></li>
            </ul>
            %import instanceOfDatabase
            %import users

            %db = instanceOfDatabase.db
            %userNick = users.session_user(db)
            %if userNick is not None:
            <ul class="right">
                <li>Logged in as {{userNick}}</li>
                <li>
                    <form action="/logout" id="logoutform" name="logoutform">
                        <input name="logout" class="waves-effect waves-light btn #c62828 red darken-3" type="submit"
                               value="Logout">
                    </form>
                </li>
            </ul>
            %else:
            <ul class="right">
                <form action="/login" method="post" id="loginform" name="loginform">
                    <li><input id="nick" name="nick" type="text" placeholder="Nickname"></li>
                    <li><input id="password" name="password" type="password" placeholder="Password"></li>
                    <li id="login" class="btn waves-effect waves-light"><input type="submit" value="Login"></li>
                </form>
            </ul>
            %end
        </div>
    </nav>
</div>

<div>
    {{!base}}
</div>

</body>
</html>
