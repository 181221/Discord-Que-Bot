

$PATH='C:\Program Files (x86)\World of Warcraft\_classic_'
$hashTable = @{}
$X_CLICK=792
$Y_CLICK=228

Function Get-Environment-Variables {
	Get-Content .env | Foreach-Object{
	   $var = $_.Split('=')
	   New-Variable -Name $var[0] -Value $var[1]
	   $hashTable.Add($var[0],$var[1])
	}
}

Get-Environment-Variables

$ACCOUNT = $hashTable['ACCOUNT']
$PASSWORD= $hashTable['PASSWORD']

[system.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms") | out-null

function Click-MouseButton
{
    [System.Windows.Forms.Cursor]::Position = New-Object System.Drawing.Point($X_CLICK,$Y_CLICK)
    $signature=@' 
      [DllImport("user32.dll",CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
      public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
'@ 

    $SendMouseClick = Add-Type -memberDefinition $signature -name "Win32MouseEventNew" -namespace Win32Functions -passThru 

        $SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
        $SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);
}

Function Login-WoW
{
	.\Wow.exe
	Start-Sleep -s 3
	$Job = Get-Process Wow | Select-Object -Property Id
	$wsh = New-Object -ComObject WScript.Shell
	$wsh.AppActivate($Job.Id)
	Start-Sleep -s 2
	$wsh.SendKeys($ACCOUNT)
	Start-Sleep -s 2
	$wsh.SendKeys("{TAB}")
	$wsh.SendKeys($PASSWORD)
	Start-Sleep -s 2
	$wsh.SendKeys("{ENTER}")
	Start-Sleep -s 4
	$wsh.SendKeys("{ENTER}")
	Start-Sleep -s 5
	Click-MouseButton
	$wsh.SendKeys("{ENTER}")
}

Function Init 
{
	Set-Location -Path $PATH
	Login-WoW
}

Init


