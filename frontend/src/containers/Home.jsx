import React from 'react';
import { Typography, Paper } from '@mui/material';

const Home = () => {
    return (
        <>
            <Paper
                sx={{
                    p: 5,
                    height: 440,
                    width: '80%'
                }}
            >
                <Typography component="h2" variant="h6" color="primary">
                    The report function is under development. <br /> <br />
                    Hi Team, We added a new section in T.M.S as Leaves. <br />
                     Use this section to apply leaves from 01/02/2023.
                    <ul> <li>Leave application through emails won't be accepted from 01/02/2023. </li>
                    <li>Leave application status should be followed up using T.M.S portal only. </li>
                    <li></li>
                    </ul>
                </Typography>
            </Paper>
        </>
    );
};

export default Home;
