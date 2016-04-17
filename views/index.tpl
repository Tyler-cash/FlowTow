% rebase('base.tpl')


<h1>Welcome to FlowTow</h1>

<div class='container'>
    <div class="row">

        <div class='image col s10 m3 offset-s1 flowtow'>
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img src="/static/images/cycling.jpg" alt="window">
                </div>
                <div class="card-content">
                    <p class='user'>Bobalooba</p>
                    <p class='likes'>3 Likes</p>
                    <p class='date'>Uploaded : 2016-01-04:19:13</p>
                </div>
                <div class="card-action">
                    <form>
                        <button action="submit /like" name="cycling.jpg"><a class="waves-effect waves-light btn">Like</a></button>
                        <input value="cycling.jpg" class="hidden">
                    </form>
                </div>
            </div>
        </div>
        <div class='image col s10 m3 offset-s1 flowtow'>
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img src="/static/images/flower.jpg" alt="window">
                </div>
                <div class="card-content">
                    <p class='user'>Bobalooba</p>
                    <p class='likes'>3 Likes</p>
                    <p class='date'>Uploaded : 2016-01-04:19:13</p>
                </div>
                <div class="card-action">
                    <form>
                        <button action="/like" name="flower.jpg"><a class="waves-effect waves-light btn">Like</a></button>
                        <input value="flower.jpg" class="hidden">
                    </form>
                </div>
            </div>
        </div>
        <div class='image col s10 m3 offset-s1 flowtow'>
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img src="/static/images/hang-glider.jpg" alt="window">
                </div>
                <div class="card-content">
                    <p class='user'>Bobalooba</p>
                    <p class='date'>Date Uploaded : 2016-01-04:19:13</p>
                    <p class='likes'>3 Likes</p>
                </div>
                <div class="card-action">
                    <form>
                        <button action="/like"><a class="waves-effect waves-light btn">Like</a></button>
                        <input value="hang-glider.jpg" class="hidden">
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>


