% rebase('base.tpl')
<div class='container' id="fileupload">
    <div class="row">
        <p>Please select an image to upload</p>
        <form id="uploadform" action="/upload" method="post" enctype="multipart/form-data">
            <ul>
                    <li id="file-select" class="file-field input-field btn waves-effect waves-light"><input
                            name="imagefile"
                            value="Select image" id="file" type="file">Select File
                    </li>
                </ul>
                <input id="submit" type="submit" class="btn waves-effect waves-light" value="submit">
        </form>
    </div>
</div>


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
        %#Prints this out len(images) times
        <div class="image col s10 m4 offset-s1 flowtow">
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <a href="/comments/{{filename}}">
                        <img draggable="false" class="user-image" src="/static/images/{{filename}}">
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
        %end

    </div>
</div>