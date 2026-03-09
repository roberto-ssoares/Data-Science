Write-Host "===================================="
Write-Host "Installing Graphviz for Diagram-as-Code"
Write-Host "===================================="

$version = "14.1.3"
$url = "https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/$version/windows_10_cmake_Release_graphviz-install-$version-win64.exe"

$tempFile = "$env:TEMP\graphviz-install.exe"
$installDir = "C:\Program Files\Graphviz"

Write-Host ""
Write-Host "Downloading Graphviz $version ..."

Invoke-WebRequest -Uri $url -OutFile $tempFile

Write-Host "Download complete."

Write-Host ""
Write-Host "Installing Graphviz silently..."

Start-Process -FilePath $tempFile -ArgumentList "/S" -Wait

Write-Host "Installation finished."

Write-Host ""
Write-Host "Adding Graphviz to PATH..."

$graphvizBin = "$installDir\bin"

$currentPath = [Environment]::GetEnvironmentVariable("Path","Machine")

if ($currentPath -notlike "*Graphviz*") {

    $newPath = $currentPath + ";" + $graphvizBin
    [Environment]::SetEnvironmentVariable("Path",$newPath,"Machine")

    Write-Host "PATH updated."

}
else {

    Write-Host "Graphviz already in PATH."

}

Write-Host ""
Write-Host "Refreshing environment..."

$env:Path += ";$graphvizBin"

Write-Host ""
Write-Host "Testing installation..."

try {
    dot -V
}
catch {
    Write-Host "Graphviz installed but PATH may require terminal restart."
}

Write-Host ""
Write-Host "Graphviz installation complete."
