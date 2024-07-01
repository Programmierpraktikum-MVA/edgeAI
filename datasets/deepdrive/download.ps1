# You may need to press some key sometime during the process
# Especially if a process takes suspiciously long, then you might need to press something
# The progress bar is deactivated, because otherwise it would be really really slow
param (
    [string]$base_url = "https://dl.cv.ethz.ch/bdd100k/data/",
    [string]$temp_dir = "tmp"
)

$ProgressPreference = 'SilentlyContinue' # Comment out this line if you want a progress bar -> it will be incredibly slow

# Ensure the necessary tools are available
if (-not (Get-Command Invoke-WebRequest -ErrorAction SilentlyContinue)) {
    Write-Output "Invoke-WebRequest is required but not installed. Aborting."
    exit 1
}
if (-not (Get-Command Expand-Archive -ErrorAction SilentlyContinue)) {
    Write-Output "Expand-Archive is required but not installed. Aborting."
    exit 1
}

function Download-Data {
    param (
        [string]$type,
        [string]$dataset
    )

    $zip_file = ""
    $zip_dir = ""
    $output_dir = ""

    if ($type -eq "dataset") {
        $zip_dir = "bdd100k/images/100k/$dataset/"
        $zip_file = "100k_images_$dataset.zip"
        $output_dir = "../images/"
    } elseif ($type -eq "labels") {
        $zip_dir = "bdd100k/labels/$dataset"
        $zip_file = "bdd100k_${dataset}_labels_trainval.zip"
        $output_dir = "../annotations/"
    } else {
        Write-Output "Invalid type specified."
        return 1
    }

    $outputPath = "$output_dir\$dataset"
    if (Test-Path -Path $outputPath -PathType Container) {
        $itemCount = (Get-ChildItem -Path $outputPath).Count
        if ($itemCount -gt 0) {
            Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') INFO: $outputPath is not empty. Assuming $type already exists and skipping download."
            return 0
        }
    }

    Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') INFO: Starting download for $zip_file"
    try {
        Invoke-WebRequest -Uri "$base_url$zip_file" -OutFile "$zip_file" -TimeoutSec 60
        Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') INFO: Unzipping $zip_file"
        Expand-Archive -Path "$zip_file" -DestinationPath "."
        New-Item -ItemType Directory -Force -Path "$output_dir"
        Move-Item -Path "$zip_dir" -Destination "$output_dir"
        Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') INFO: Successfully downloaded and extracted $zip_file"
    } catch {
        Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') ERROR: Failed to download or unzip $zip_file."
        return 1
    }
}

New-Item -ItemType Directory -Force -Path $temp_dir
Set-Location -Path $temp_dir

Download-Data -type "dataset" -dataset "train"
Download-Data -type "dataset" -dataset "val"
Download-Data -type "dataset" -dataset "test"
Download-Data -type "labels" -dataset "det_20"

Write-Output "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') INFO: Cleaning up temporary resources."
Set-Location -Path ..
Remove-Item -Recurse -Force -Path $temp_dir