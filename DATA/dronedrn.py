def main():
    import exiftool
    import glob
    import pandas as pd
    rute='/home/adolfo/ohw23_proj_drone_georef/DATA/'
    files = glob.glob(f'{rute}*.JPG', recursive = True)
    files2=sorted(files, key=lambda x: (x.split('/')))
    with exiftool.ExifTool() as et:
        metadata = et.execute_json(*files2)
        df_meta = pd.DataFrame(metadata)
    want=['SourceFile',   
    'EXIF:GPSLatitudeRef',
    'EXIF:GPSLatitude',
    'EXIF:GPSLongitudeRef',
    'EXIF:GPSLongitude',
    'EXIF:GPSAltitudeRef',
    'EXIF:GPSAltitude',
    'XMP:RtkFlag',
    'XMP:DewarpFlag',
    'XMP:AbsoluteAltitude',
    'XMP:RelativeAltitude',
    'XMP:GPSLatitude',
    'XMP:GPSLongtitude',
    'XMP:GimbalRollDegree',
    'XMP:GimbalYawDegree',
    'XMP:GimbalPitchDegree',
    'XMP:FlightRollDegree',
    'XMP:FlightYawDegree',
    'XMP:FlightPitchDegree',
    'XMP:CamReverse',
    'XMP:GimbalReverse',
    'XMP:CalibratedFocalLength',
    'XMP:CalibratedOpticalCenterX',
    'XMP:CalibratedOpticalCenterY',]
    df_metasub=df_meta[want]
    df_metasub.to_csv('drone.csv')

if __name__ == "__main__":
    main()

