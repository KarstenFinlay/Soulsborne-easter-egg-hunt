# check if build is enforced

param (
    [Parameter(HelpMessage="Rebuilds image. Overwriting existing one")]
    [switch]$build = $false,

    [Parameter(HelpMessage="Whether result from run should be saved on local")]
    [switch]$save = $false
)

# run from project root

if (-not(Test-Path -Path ".\Dockerfile")) {
    Write-Host "Could not locate Dockerfile. Run launch script from project root."
    exit 1
}

# check whether image exists. If not; always build

docker inspect --type image easter_souls_app >$null 2>&1

if ($?) {
    if ($build) {
        Write-Host "Easter Souls image already exists. Deleting..."
        docker rmi easter_souls_app
    }
} else {
    $build = $true
}

# build image when necessary

if ($build) {
    Write-Host "Creating image..."
    docker build -t easter_souls_app:latest .
}

# run image

docker run -it --name easter_souls easter_souls_app:latest

# check run was successful

if (-not($?)) {
    Write-Host "Unexpected failure while running container."
    docker rm easter_souls >$null 2>&1
    exit 1
} else {
    if (-not($save)) {
        docker rm easter_souls >$null 2>&1
        exit 0
    } else {
        Write-Host "Run was successful. Getting results..."
    }
}

# check results directory exists

if (-not(Test-Path -Path ".\Results")) {
    Write-Host "No Results directory found. Creating..."
    New-Item -Path "." -Name "Results" -ItemType "directory"
}

# copy result file from docker container to local results

docker container cp easter_souls:/usr/src/Results/. ./Results/

# remove container

docker rm easter_souls >$null 2>&1
