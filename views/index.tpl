% rebase('base.tpl')


<h1 class="center" id="welcome-message"><strong>Welcome to FlowTow</strong></h1>

<div class='container'>
    <div class="row">
        %import instanceOfDatabase
        %import interface

        %db = instanceOfDatabase.db

        %images = interface.list_images(db, 3)
        %for image in images:
        % user = image['user']
        % likes = image['likes']
        % timestamp = image['timestamp']
        % filename = image['filename']
        <div class="image col s10 m3 offset-s1 flowtow">
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
                        <input type="submit" value="Like" action="/like"><a class="waves-effect waves-light btn">Like</a></input>
                        <input name="filename" value="{{filename}}" class="hidden">
                    </form>
                </div>
            </div>
        </div>
        %end

    </div>
</div>

