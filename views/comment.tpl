% rebase('base.tpl')

<div class='container'>
    <div class="row">
        %import instanceOfDatabase
        %import interface
        %import comments
        %import users
        %import bottle
        %db = instanceOfDatabase.db

        %filename = bottle.request.get_cookie('filename')
        %image = interface.get_image(db, filename)
        %user = image[2]
        %timestamp = image[1]
        %filename = image[0]
        %likes = interface.count_likes(db, filename)
        %bottle.response.delete_cookie('filename')
        <div class="col s3 m2 hidden">Teeestt</div>
        <div id="comment-image" class="image col s10 m6 offset-s1 flowtow">
            <div class="card">
                <div class="fullscreen-image waves-effect waves-block waves-light">
                    <a href="/comments/{{filename}}">
                        <img draggable="false" class="fullscreen-image" src="/static/images/{{filename}}">
                    </a>
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
        <div class="col s10 m5 " id="comment-container">
            <h3>Comments</h3>
            %comments = comments.list_comments(db,filename, 10)
            %if len(comments) is 0:
            <div class="card-panel red lighten-2 white-text">
                <span>Sorry, There are no comments for this image.</span>
            </div>
            %else:
            % for comment in comments:
            % text = comment[3]
            % user = comment[1]
            % date = comment[2]
            <div class="card-panel  comment blue lighten-4">
                <ul>
                    <p><strong>Username</strong> : {{user}}</p>
                    <p><strong>Date posted</strong> : {{date}}</p>
                </ul>
                <p>{{text}}</p>
            </div>
            %end
            %end
            %if users.session_user(db) is not None:
            <form action="/submit-comment" method="post">
                <input name="comment" placeholder="What do you have to say?">
                <input class="hidden" name="filename" value="{{filename}}">
                <input type="submit" class="hidden">
            </form>
            %end
        </div>
    </div>
</div>