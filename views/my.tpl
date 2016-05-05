% rebase('base.tpl')

<div class='container'>
    <div class="row">
        %import instanceOfDatabase
        %import interface
        %import users
        %db = instanceOfDatabase.db

        %usernick = users.session_user(db)
        %images = interface.list_images(db, 3, usernick)
        %for image in images:
        % user = image['user']
        % likes = image['likes']
        % timestamp = image['timestamp']
        % filename = image['filename']
        <div class="image col s10 m4 offset-s1 flowtow">
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img draggable="false" src="/static/images/{{filename}}" alt="cycling.jpg">
                </div>
                <div class="card-content">
                    <p class="user">{{user}}</p>
                    <p class="likes">{{likes}}</p>
                    <p class="date">Uploaded : {{timestamp}}</p>
                </div>
                <div class="card-action center">
                    <form action="/like" class="like-image" method="post">
                        <input type="hidden" name="filename" value="{{filename}}">
                        <input type="submit" value="Like" class="waves-light btn">
                    </form>
                </div>
            </div>
        </div>
        %end

    </div>
</div>